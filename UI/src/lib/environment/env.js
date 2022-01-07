const myVars = {
    API_URL: import.meta.env.VITE_API_URL,
}
//console.log(myVars);
//console.log(import.meta.env);
//thrown when an evironmental variable is not set when it is required
class EnvironmentError extends Error {
    constructor(message) {
        super(message);
        this.name = 'EnvironmentError';
    }
}

// get an environment variable
export const envVar = (varToGet) => {
    if (myVars[varToGet] !== undefined) {
            return myVars[varToGet];
    } else {
        throw new EnvironmentError(`${varToGet} is not set in the environment`);
    }
};

export default envVar;