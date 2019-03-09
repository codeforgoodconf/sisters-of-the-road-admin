import { RECIEVE_SEARCH_QUERY, CLEAR_SEARCH_QUERY } from '../../actions/account_actions'


const searchQueryReducer = (state=[], action) => {
    Object.freeze(state);

    switch(action.type) {
        case RECIEVE_SEARCH_QUERY:
            return action.accounts;
        case CLEAR_SEARCH_QUERY:
            return [];
        default:
            return state;
    };
};


export default searchQueryReducer;