import { browser } from '$app/env';
if (browser) {
    throw new ClientSideImportError("This module cannot be imported client-side.");
}

//thrown when this module is imported in the wrong place
class ClientSideImportError extends Error {
    constructor(message) {
        super(message);
        this.name = 'ClientSideImportError';
    }
}

