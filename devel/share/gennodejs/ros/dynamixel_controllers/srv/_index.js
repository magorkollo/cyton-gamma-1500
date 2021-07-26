
"use strict";

let SetComplianceSlope = require('./SetComplianceSlope.js')
let SetCompliancePunch = require('./SetCompliancePunch.js')
let StartController = require('./StartController.js')
let StopController = require('./StopController.js')
let RestartController = require('./RestartController.js')
let SetSpeed = require('./SetSpeed.js')
let TorqueEnable = require('./TorqueEnable.js')
let SetComplianceMargin = require('./SetComplianceMargin.js')
let SetTorqueLimit = require('./SetTorqueLimit.js')

module.exports = {
  SetComplianceSlope: SetComplianceSlope,
  SetCompliancePunch: SetCompliancePunch,
  StartController: StartController,
  StopController: StopController,
  RestartController: RestartController,
  SetSpeed: SetSpeed,
  TorqueEnable: TorqueEnable,
  SetComplianceMargin: SetComplianceMargin,
  SetTorqueLimit: SetTorqueLimit,
};
