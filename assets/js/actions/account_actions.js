import * as ApiUtils from '../utils/api_utils';

export const RECIEVE_SEARCH_QUERY = 'RECIEVE_SEARCH_QUERY';
export const RECIEVE_ACCOUNT = 'RECIEVE_ACCOUNT';
export const CLEAR_SEARCH_QUERY = 'CLEAR_SEARCH_QUERY';
export const RECIEVE_BUY_ERROR = 'RECIEVE_BUY_ERROR';
export const CLEAR_ERRORS = 'CLEAR_ERRORS'

export const recieveSearchQuery = (accounts) => ({
    type: RECIEVE_SEARCH_QUERY,
    accounts
});

export const clearSearchQuery = () => ({
    type: CLEAR_SEARCH_QUERY
});

export const recieveAccount = (account) => ({
    type: RECIEVE_ACCOUNT,
    account
});

export const recieveBuyError = (error) => ({
    type: RECIEVE_BUY_ERROR,
    error
});

export const clearErrors = () => ({
    type: CLEAR_ERRORS
})



export const requestSearchQuery = (searchQuery) => dispatch => (
    ApiUtils.fetchSearchQuery(searchQuery)
    .then(
        (response) => dispatch(recieveSearchQuery(response.data))
    )
);

export const buyCard = (account, amount) => dispatch => (
    ApiUtils.buyCard(account, amount)
    .then((response) => {
        if (response.data.error) return dispatch(recieveBuyError(response.data.error))
            
        return dispatch(recieveAccount(response.data))
        }
    )
);

export const buyMeal = (account, amount) => dispatch => (
    ApiUtils.buyMeal(account, amount)
    .then((response) => {
        if (response.data.error) return dispatch(recieveBuyError(response.data.error))
            
        return dispatch(recieveAccount(response.data))
        }
    )
);


export const credit = (account, amount) => dispatch => (
    ApiUtils.credit(account, amount)
    .then((response) => {
        if (response.data.error) return dispatch(recieveBuyError(response.data.error))
            
        return dispatch(recieveAccount(response.data))
        }
    )
);


