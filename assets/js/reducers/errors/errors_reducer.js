import { combineReducers } from 'redux';

import BuyErrorReducer from './buy_error_reducer'


export const errorReducer =  combineReducers({
    buyError: BuyErrorReducer
});


export default errorReducer;