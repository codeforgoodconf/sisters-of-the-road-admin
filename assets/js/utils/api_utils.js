import axios from 'axios';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export const fetchSearchQuery = (searchQuery) => {
    return axios.get('/account/search?q=' + searchQuery)
};

