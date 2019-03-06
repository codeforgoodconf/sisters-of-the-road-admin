import { fetchSearchQuery } from '../utils/api_utils';

export const RECIEVE_SEARCH_QUERY = 'RECIEVE_SEARCH_QUERY';
export const RECIEVE_ACCOUNT = 'RECIEVE_ACCOUNT'

export const recieveSearchQuery = (accounts) => ({
    type: RECIEVE_SEARCH_QUERY,
    accounts
})

export const recieveAccount = (account) => ({
    type: RECIEVE_ACCOUNT,
    account
})


export const requestSearchQuery = (searchQuery) => dispatch => (
    fetchSearchQuery(searchQuery)
    .then(
        (response) => dispatch(recieveSearchQuery(response.data))
    )
)