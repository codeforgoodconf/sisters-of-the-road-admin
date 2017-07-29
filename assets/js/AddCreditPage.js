import React, { Component } from 'react';


class AddCreditPage extends Component {
    constructor () {
        super();
    }

    render () {
        const {
            account
        } = this.props;
        return (
            <div className="AddCreditPage">
                <div>
                    <h3>{account.name}</h3>
                    <h5>Last worked: {account.lastWorked}</h5>
                    <h5>Last meal: {account.lastMeal}</h5>
                </div>
                <div>
                    Hours Worked: 
                    <input type="number" min="0.00" step="0.25" max="2500" />
                </div>
                <div>
                    <button>
                        Add amount
                    </button>
                </div>
                <button onClick={() => this.props.switchView('accountpage', account)}>
                    Cancel
                </button>
            </div>
         );
    }
}

export default AddCreditPage;
