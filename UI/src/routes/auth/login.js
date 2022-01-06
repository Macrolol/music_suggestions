import { generateToken } from "$lib/auth/jwt";
import { apiPost } from "$lib/apiAccess/api";


export const post = async (request) => {

    if (request.body.email_address && request.body.password) {
    try{
        const user = await apiPost({path : '/login', data : request.body});
        console.log(user);
        const token = generateToken(user);

        return {
            status : 200,
            headers : {
                "Set-Cookie" : `token=${token}; HttpOnly; SameSite=Strict; Max-Age=${60 * 60}`
            },
            body : {
                token : token,
                user : user
            }
        }
    } catch (err) {
        return {
            status : 500,
            body : {
                error : err.message
            }
        }
    }
}
       
};