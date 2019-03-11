import { RECIEVE_BUY_ERROR, RECIEVE_ACCOUNT } from '../../actions/account_actions';

const buyErrorReducer = (state = null, action) => {
    Object.freeze(state);

    switch (action.type) {
        case RECIEVE_BUY_ERROR:
            return action.error;
        case RECIEVE_ACCOUNT:
            return null;
        default:
            return state;
    }
};

export default buyErrorReducer;