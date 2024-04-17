import api from './api';
import Cookies from 'js-cookie';

export const fetchAsciiKey = async () => {

    const token = localStorage.getItem('token');

    try {
        const response = await api.get('/ascii', {
            headers: {
                Authorization: token,
            },
        });
        const { key } = response.data;
        localStorage.setItem("key", key)
        return response.status;
    } catch (error) {
        localStorage.clear()
        return error.response.status ;
    }
};

export const getAuthorization = async () => {

    const token = localStorage.getItem('token');
    const data = {
        id : JSON.parse(localStorage.getItem('user')).session,
        key1 : localStorage.getItem('admin'),
        key2 : Cookies.get('admin')
    }

    try {
        const response = await api.post('/offset', data, {
            headers: {
                Authorization: token,
            },
        });

        return response.data
    } catch(error) {
        if (error.response.status === 401) {
            return { status: 401, message: "Veuillez vous connecter" };
        } else {
            return { status: error.response.status , message: "Une erreur s'est produite. Veuillez réessayer plus tard" };
        }        
    }
}