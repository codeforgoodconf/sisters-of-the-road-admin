import { RECIEVE_ACCOUNT } from '../../actions/account_actions'


const accountReducer = (state= {}, action) => {
    Object.freeze(state);

    switch (action.type) {
        case RECIEVE_ACCOUNT:
            return action.account;
        default:
            return state;
    }
}

export default accountReducer;