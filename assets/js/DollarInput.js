import React, { Component } from 'react';


class DollarInput extends Component {
    constructor () {
        super();
        this.state = {
            amount: ''
        };
    }

    onAmountChange (amount) {
        const {
            updateAmount
        } = this.props;

        if (amount === undefined) {
            return;
        }

        let amountStr = String(amount).replace('.', ''),
            len = amountStr.length;
        if (len === 1) {
            amountStr = amountStr + '.00';
        } else if (len === 2) {
            amountStr = amountStr.slice(0, 1) + '.' + amountStr.slice(1, 2) + '0';
        } else {
            amountStr = amountStr.slice(0, len - 2) + '.' + amountStr.slice(len - 2, len);
        }

        if (isNaN(Number(amountStr))) {
            this.setState({amount: ''});
        } else {
            this.setState({amount: Number(amountStr)});
        }

        updateAmount(amount);
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
