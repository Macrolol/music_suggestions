
//This is an error that is thrown when the user is not authenticated
export class AuthenticationError extends Error{
    constructor(...params){
        super(...params);
        this.name = 'AuthenticationError';

    }
}

