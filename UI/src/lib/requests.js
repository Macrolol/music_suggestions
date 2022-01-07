
class RequestError extends Error {
    constructor(message, status, response) {
        super(message);
        this.status = status;
        this.response = response
        this.name = 'RequestError';
    }
}

// found a pattern similar to this in one of the sveltekit examples
// here: https://github.com/sveltejs/realworld/blob/master/src/lib/api.js
// returns a promise with the json response
const sendRequest = async ({method, path, data, auth}) => {
    //get the request options ready
    const options = { 
        method,
        headers: {},
    };
    
    //if we have data, we need to set the body
    if (data) {
        options.headers['Content-Type'] = 'application/json';
        options.body = JSON.stringify(data);
    }

    //if we have an auth token, add it to the headers
    if (auth) {
        options.headers['Authorization'] = `Bearer ${auth}`;
    }

    //console.debug(`Sending request to ${path}`);
    // send the request to the api at the path specified with the options
    let response = await fetch(path, options)
    //if the response is ok return the response in json format
    if (response.ok) {
        return await response.json();
    }
    //otherwise throw an error
    throw new RequestError(response.statusText, response.status, response);
};


// define and export the postRequest function that sends a
// post request using the sendRequest function
export const postRequest = async ({path, data, auth}) => {
    return sendRequest({method :'POST', path, data, auth});
}

// define and export the getRequest function that sends a
// get request with no data using the sendRequest function
export const getRequest = async ({path, auth}) => {
    return sendRequest({method : 'GET', path, auth});
}
