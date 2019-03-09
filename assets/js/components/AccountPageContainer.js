import { connect } from 'react-redux';

import AccountPage from './AccountPage';

import { clearSearchQuery } from '../actions/account_actions';


const mapStateToProps = (state) => ({
    account: state.entities.account
});

const mapDispatchToProps = () => dispatch => ({
    clearSearchQuery: () => dispatch(clearSearchQuery())
});

export default connect(mapStateToProps, mapDispatchToProps)(AccountPage);