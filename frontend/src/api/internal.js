import axios from "axios"

const HOST = process.env.API_HOST || "0.0.0.0";
const PORT = process.env.API_PORT || 5000;
const PROTOCOL = process.env.API_PROTOCOL || "http";
const API_PREFIX = process.env.API_PREFIX || null;


const apiPrefix = API_PREFIX === null ? "" : `/${API_PREFIX}/`;

const api = axios.create({
    baseURL: `${PROTOCOL}://${HOST}:${PORT}${apiPrefix}`,
})


export { api }