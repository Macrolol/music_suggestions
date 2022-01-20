import cookie from 'cookie';

const cookieOptions = {
        maxAge : 60 * 60 * 24,
        httpOnly : true,
        sameSite : true,
        path : '/'
    }

const removeCookieOptions = {
        expires : new Date(0),
        httpOnly : true,
        sameSite : true,
        path : '/'
}
    

/* options = { 
    setCookies : [{name : value}], //ease of use cookie options
    removeCookies : [name],
    setCookie : name,
    removeCookie : name
    headers : {}
} */
const buildResponse = ({status, body, options}) => {
    body = body || {};
    const headers = options ? options.headers || {} : {}; // set headers to either options.headers or an empty object;
    headers['Set-Cookie'] = headers['Set-Cookie']  || [];
    if (options) {
        if (options.setCookies && options.setCookies.length) {
            
                headers['Set-Cookie'] = headers['Set-Cookie'].concat(
                options.setCookies.map(
                    cookieToSet => {
                        return cookie.serialize(cookieToSet.name, cookieToSet.value, cookieOptions);
                    }
                )
            );

        } else if (options.setCookie) {
            headers['Set-Cookie'].push(cookie.serialize(options.setCookie.name, options.setCookie.value, cookieOptions));
        }

        if (options.removeCookies && options.removeCookies.length) {
            
                headers['Set-Cookie'] = headers['Set-Cookie'].concat(
                options.removeCookies.map(
                    cookieToRemove => {
                        value = cookie.serialize(cookieToRemove, '', removeCookieOptions)
                        //console.debug(`Removing cookie: ${value}`); // debug
                        return value; 
                    }
                )
            );
           

        } else if (options.removeCookie) {
            headers['Set-Cookie'].push(cookie.serialize(options.removeCookie, '', removeCookieOptions));
        }
    }
    //console.debug(headers['Set-Cookie']); //debug
    return {
        status,
        headers,
        body
    };
}


/* options = { 
    setCookies : [{name : value}],
    removeCookies : [name],
    setCookie : name,
    removeCookie : name
} */
export const okResponse = ({ status, body, options}) => {
   status = status || 200; 
   return buildResponse({status, body, options});
}

export const errorResponse = ({status, body, options}) => {
    status = status || 500;
    body = body || { message : 'Internal server error' };
    return buildResponse({status, body, options});
}
