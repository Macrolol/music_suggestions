import { okResponse } from "$lib/responseBuilder";

export const post = async (request) => {
    console.log("Post Logout.js");
    return okResponse({options : { removeCookie : 'token' }});
}