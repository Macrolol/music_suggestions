

export const get = async (request) => {
    return {
        status : 200,
        headers : {
            "Set-Cookie" : `token=; HttpOnly; SameSite=Strict; Max-Age=0`
        }
    };
}