import { errorResponse } from "$lib/responseBuilder";
import cookie from 'cookie';
import { verifyToken } from "$lib/auth/jwt.js";

// This function returns ErrorResonses if things go wrong.
export const proccessCookies = async (request) => {
    
    if (request.headers.cookie) {

        const cookies = cookie.parse(request.headers.cookie); //parse the cookies
        console.debug(`Cookies: ${JSON.stringify(cookies)}`); //debug


        //dealing with jwt cookies
        const token = cookies.token;
        if (token) {
            try {
                const { user } = await verifyToken(token);
                delete cookies.token;
                request.locals.user = user;
                if (!request.headers.authorization) {
                    request.headers.authorization = `Bearer ${token}`;
                }
            } catch (err) {
                if (err.name === 'TokenExpiredError') {
                    return errorResponse({
                        status : 410 ,
                        body : {
                            message: 'Token expired'
                        }, 
                        options: { 
                            removeCookie: 'token' 
                        } 
                    });
                } else if (err.name === 'JsonWebTokenError') {
                    return errorResponse({
                        status: 401,
                        body: {
                            message: 'Invalid token'
                        }
                        , options: {
                            removeCookie: 'token'
                        }
                    });
                }
                console.log("Error: ", err);
                return errorResponse({});
            }
        }

        

        //if there are extra cookies, remove them
        const remainingCookies = Object.keys(cookies);
        if (remainingCookies.length) {
            console.debug(`Remaining cookies: ${JSON.stringify(remainingCookies)}`); //debug
            return errorResponse({
                status: 402,
                body: {
                    message: 'Invalid cookies'
                },
                options: {
                    removeCookies: remainingCookies
                }
            });
        }
    }
}