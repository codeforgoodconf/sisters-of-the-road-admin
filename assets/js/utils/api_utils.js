import axios from 'axios';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export const fetchSearchQuery = (searchQuery) => (
     axios.get('/account/search?q=' + searchQuery)
);

export const buyCard = (account, amount, initials) => (
    axios.post('/account/' + account.account_id + '/buy_card', { amount, initials })
);


export const buyMeal = (account, amount, initials) => (
    axios.post('/account/' + account.account_id + '/buy_meal', { amount, initials })
);

export const credit = (account, amount, initials) => (
    axios.post('/account/' + account.account_id + '/credit', { amount, initials })
);