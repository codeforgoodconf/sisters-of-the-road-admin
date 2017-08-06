import React, { Component } from 'react';

class ConfirmationPage extends Component {
    constructor () {
        super();
    }

    render () {
        const {
            account
        } = this.props;
       
        return (
            <div className="ConfirmationPage">
                <div className="header col-sm-12 centered">
                    <h3>{account.name}</h3>
                </div>
                <div id="calculate" className="jumbotron row center-block">
                    <div className="total">
                        {account.lastAdded > 0 &&
                            <h3 className="text-center">Amount added: ${account.lastAdded / 100}</h3>
                        }
                        {account.lastAdded < 0 &&
                            <h3 className="text-center">Amount spent: ${(account.lastAdded * -1) / 100}</h3>
                        }
                                                
                        <h3 className="text-center">New balance: ${account.currentCredit / 100}</h3>
                    </div>
                </div>
                
                <button className="btn btn-info col-sm-offset-5 center-block" onClick={() => this.props.switchView('searchpage')}>
                    Back to Search
                </button>
            </div>
         );
    }
}

export default ConfirmationPage;
