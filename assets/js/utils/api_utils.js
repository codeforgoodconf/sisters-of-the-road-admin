import axios from 'axios';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export const fetchSearchQuery = (searchQuery) => (
     axios.get('/account/search?q=' + searchQuery)
);

export const buyCard = (account, amount) => (
    axios.post('/account/' + account.account_id + '/buy_card', { amount })
);


export const buyMeal = (account, amount) => (
    axios.post('/account/' + account.account_id + '/buy_meal', { amount })
);

export const credit = (account, amount) => (
    axios.post('/account/' + account.account_id + '/credit', {amount: amount})
)