import * as ApiUtils from '../utils/api_utils';

export const RECIEVE_SEARCH_QUERY = 'RECIEVE_SEARCH_QUERY';
export const RECIEVE_ACCOUNT = 'RECIEVE_ACCOUNT'
export const CLEAR_SEARCH_QUERY = 'CLEAR_SEARCH_QUERY'

export const recieveSearchQuery = (accounts) => ({
    type: RECIEVE_SEARCH_QUERY,
    accounts
})

export const clearSearchQuery = () => ({
    type: CLEAR_SEARCH_QUERY
})

export const recieveAccount = (account) => ({
    type: RECIEVE_ACCOUNT,
    account
})


export const requestSearchQuery = (searchQuery) => dispatch => (
    ApiUtils.fetchSearchQuery(searchQuery)
    .then(
        (response) => dispatch(recieveSearchQuery(response.data))
    )
)

export const buyCard = (account, amount) => dispatch => {


    
    
    return ApiUtils.buyCard(account, amount)
    .then((response) => {
        let account = account
        debugger
    })
}