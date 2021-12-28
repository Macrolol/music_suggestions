
//This is an error that is thrown when the user is not authenticated
export class AuthenticationError extends Error{
    constructor(...params){
        super(...params);
        this.name = 'AuthenticationError';

        // Maintains proper stack trace for where our error was thrown (only available on V8)
        if (Error.captureStackTrace) {
            Error.captureStackTrace(this, CustomError)
        }

    }
}

