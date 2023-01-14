const mongoose = require("mongoose")
const jwt = require("jsonwebtoken")
const Joi = require("joi")
const passwordComplexity = require('joi-password-complexity')

const userSchema = new mongoose.Schema({
    username: {type: String, required: true},
    email: {type: String, required: true},
    password: {type: String, required: true},
    phone: {type: String, required: true}
})

userSchema.methods.generateAuthToken = function(){
    const token = jwt.sign({_id: this_id}, process.env.JWTPRIVATEKEY, {expiresIn: "7d"})
    return token
}

const User = mongoose.model("user", userSchema)

const validate = (data) => {
    const schema = Joi.object({
        username: Joi.string().required().label("username"),
        email: Joi.email().required().label("email"),
        phone: Joi.string().required().label("phone number"),
        password: passwordComplexity().required().label("password")
    })
    return schema.validate(data)
}

module.exports = {User, validate}