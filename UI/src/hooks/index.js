import { verifyToken } from "$lib/auth/jwt"
import cookie from 'cookie';

export const handle = async ({request, resolve}) => {

    if (request.headers.cookie) {
   
        try{
            const token = cookie.parse(request.headers.cookie).token;
            const { user } = await verifyToken(token);
            request.locals.user = user;
            if (!request.headers.authorization) {
                request.headers.authorization = `Bearer ${token}`;
            }
        } catch (err) {
            console.log(err);
            return {status : 500, body : {error : `Token Error ${err.message}, maybe login again`}}; 
        }
    }
    return resolve(request);
}

export const getSession = (request) => {
    if (request.locals.user) {
        return {user : request.locals.user};
    }
    return {};
}