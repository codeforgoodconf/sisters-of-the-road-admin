import React from 'react';
import { connect } from 'react-redux';
import { Route, Redirect, withRouter } from 'react-router-dom';

const Selected = ({component: Component, path, accountSelected, exact }) => (
    <Route path={path} exact={exact} render={(props) => (
        accountSelected ? (
            <Component {...props} />
        ) : (
            <Redirect to='/' />   
        )
    )}/>
)


const mSTP = state => (
    {accountSelected: Boolean(state.entities.account.account_id)}
)

export const SelectedRoute = withRouter(connect(mSTP)(Selected));

