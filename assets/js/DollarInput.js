import React, { Component } from 'react';


class DollarInput extends Component {
    constructor () {
        super();
        this.state = {
            amount: ''
        };
    }

    onAmountChange (amount) {
        this.setState({amount: amount});
        this.props.updateAmount(amount);
    }

    render () {
        return (
            <input id="amount"
                className="numbers col-sm-offset-3 input-lg center-block text-center"
                type="number"
                min="0"
                step="0.25"
                value={this.state.amount}
                placeholder={0}
                onChange={(event) => this.onAmountChange(event.target.value)} /> 
         );
    }
}


export default DollarInput;
