import jwt from 'jsonwebtoken';

const sign = jwt.sign;
const verify = jwt.verify;

export const generateToken = (user) => {
    const token = sign({user: user}, process.env.JWT_SECRET, {
        subject : user.tag,
        expiresIn: '1h',
    });
    return token;
}

export const verifyToken = async (token) => {
    const user = await verify(token, process.env.JWT_SECRET, (err, decoded) => {
        if (err) {
            throw err;
        }
        return decoded;
    });
    return user;
}

export default { generateToken, verifyToken };