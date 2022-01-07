import {proccessCookies} from './processCookies.js';

export const handle = async ({request, resolve}) => {

    const cookieErrorResponse = await proccessCookies(request);    
    if (cookieErrorResponse) {
        return cookieErrorResponse;
    }

    const response = await resolve(request);
    console.log(response);
    return response;
}

export const getSession = (request) => {
    if (request.locals.user) {
        return {user : request.locals.user};
    }
    return {};
}