import { apiPost } from "$lib/apiAccess/api";
import { errorResponse, okResponse } from "$lib/responseBuilder";
import { validateEmail } from "$lib/validateEmail";
import { RequestError } from "$lib/requests.js";



export const post = async (request) => {
    console.log("Post register.js");
    if (request.body.email_address && request.body.password && request.body.username) {
        if (validateEmail(request.body.email_address)) {
            try {
                console.log("'VALID' request: " + JSON.stringify(request));
                const response = await apiPost({
                    path: '/register',
                    data : {
                        email_address : request.body.email_address, 
                        password : request.body.password,
                        username : request.body.username
                    }
                });
                return okResponse({status : response.status});
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
                return errorResponse({
                    status : 500,
                    body: {
                        errorType : err.name,
                        message : err.message
                    }
                });
            }
        }
        return errorResponse({status : 400, body : {error : 'Invalid email address'}});
    }

    return errorResponse({status : 400, body : {error : 'Bad Request'}});
};