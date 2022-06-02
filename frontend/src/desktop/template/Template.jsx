import {Component} from 'react';
import Header from './header/Header';
import {Backdrop, CircularProgress} from '@mui/material';

import AsideMenu from './aside/Aside';
import Modals from '../../constants/Modals';
import LogInModal from '../modals/LogInModal';
import PropTypes from 'prop-types';
import {connect} from 'react-redux';

import './Template.scss';
import '../modals/scss/Common.scss';
import SignUpModal from '../modals/SignUpModal';


class Template extends Component {
    renderModals = () => {
        const {global: {modal}} = this.props;
        return (
            <>
                <LogInModal open={modal === Modals.LOG_IN}/>
                <SignUpModal open={modal === Modals.SIGN_UP}/>
            </>
        )
    }

    renderMain = () => {
        if (this.props.navigation) {
            return (
                <div className="content-container--split">
                    {<AsideMenu/>}
                    {this.props.children}
                </div>
            )
        }
        return (
            <div className="content-container">
                {this.props.children}
            </div>
        );
    }

    render = () => {
        return (
            <div className={`template ${this.props.className}`}>
                <Header />
                <main>
                    {this.renderMain()}
                </main>
                <Backdrop
                    sx={{color: '#fff', zIndex: (theme) => theme.zIndex.drawer + 1}}
                    open={this.props.global.screenSpinner}
                >
                    <CircularProgress color="inherit" />
                </Backdrop>
                {this.renderModals()}
            </div>
        )
    }
}


Template.propTypes = {
    navigation: PropTypes.bool
}

const mapStateToProps = (state) => ({
    global: state.global
})

export default connect(mapStateToProps)(Template);