import {API_URL} from "./consts";
import axios from "axios";
const instance = axios.create({
    baseURL: API_URL,
});


export async function getSummurytext(num, text) {
    const response = await instance.post(`${num}`, {text});
    console.log(response.data)
    return response.data;
}