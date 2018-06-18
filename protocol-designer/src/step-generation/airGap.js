// @flow
// import * as errorCreators from './errorCreators'
import type {RobotState, CommandCreator, AirGapArgs} from './'

/** Perform air gap with given args. Requires tip. */
const airGap = (args: AirGapArgs): CommandCreator => (prevRobotState: RobotState) => {
  const airGapCommand = {
    command: 'air-gap',
    params: {
      pipette: args.pipette,
      volume: args.volume
    }
  }

  return {
    commands: [airGapCommand],
    robotState: prevRobotState
  }
}

export default airGap
