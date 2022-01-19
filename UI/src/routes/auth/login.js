import { generateToken } from "$lib/auth/jwt";
import { apiPost } from "$lib/apiAccess/api";
import { okResponse, errorResponse } from '$lib/responseBuilder';
import { RequestError } from "$lib/requests";


export const post = async (request) => {

    if (request.body.email_address && request.body.password) {
        try{
            const user = await apiPost({path : '/login', data : request.body});
            //console.log(user);
            const token = generateToken(user);

            const responseOptions = {
                setCookie : {name : 'token', value : token}
            }

            return okResponse({
                body : {user}, 
                options : responseOptions
            });
        } catch (err) {
            if (err instanceof RequestError) {
            return errorResponse({
                status : err.status,
                body : {
                    errorType : err.name,
                    message : err.message,
                    responseFromApi : err.response
                }
            });
            }
            console.log("Error: ", err);
            return errorResponse({});
        }      
    }
    return errorResponse({
        status : 400,
        body : {
            error : 'Bad Request'
        }
    });
};