import { envVar } from '$lib/environment/env';
import { getRequest, postRequest } from '$lib/requests';


const apiUrl = envVar('API_URL');
//console.log(apiUrl);




// define export the postRequest function that sends a
// post request using the sendRequest function
export const apiPost = async ({ path, data, auth}) => {
    return postRequest({path : `${apiUrl}${path}`, data, auth});
}

// define export the getRequest function that sends a
// get request with no data using the sendRequest function
export const apiGet = async ({path, auth}) => {
    return getRequest({path : `${apiUrl}${path}`, auth});
}
