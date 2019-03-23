import { connect } from 'react-redux';

import BuyCardPage from './BuyPage'

import { buyMeal } from '../actions/account_actions'

const mapStateToProps = (state) => ({
    account: state.entities.account,
    error: state.errors.buyError,
    title: "Buy Card"
});

const mapDispatchToProps = dispatch => ({
    action: (account, amount, initials) => dispatch(buyCard(account, amount, initials))
})


export default connect(mapStateToProps, mapDispatchToProps)(BuyCardPage)