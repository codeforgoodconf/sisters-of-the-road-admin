import { RECIEVE_SEARCH_QUERY } from '../../actions/account_actions'


const searchQueryReducer = (state={}, action) => {
    Object.freeze(state);

    switch(action.type) {
        case RECIEVE_SEARCH_QUERY:
            return action.accounts;
        default:
            return state;
    };
};


export default searchQueryReducer;