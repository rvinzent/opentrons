// @flow
import * as React from 'react'

type UploadFn = (event: SyntheticInputEvent<HTMLInputElement>) => mixed

type Props = {
  /** callback to be performed with file body */
  onFileLoad: (fileBody: ?string) => mixed,
  /** render prop.
    * onChange should be passed to file input.
    * isLoading is true while the file is being read.
    */
  render: ({
    onChange: UploadFn,
    isLoading: boolean
  }) => React.Node
}

type State = {
  isLoading: boolean
}

class FileUpload extends React.Component<Props, State> {
  constructor (props: Props) {
    super(props)
    this.state = {isLoading: false}
  }

  onChange: UploadFn = (event) => {
    const file = event.currentTarget.files[0]
    const reader = new FileReader()

    reader.onload = readEvent => {
      const result = readEvent.currentTarget.result
      this.props.onFileLoad(result)
      this.setState({isLoading: false})
    }

    this.setState({isLoading: true}, () => {
      reader.readAsText(file)
    })

    // reset the state of the input to allow file re-uploads
    event.currentTarget.value = ''
  }

  render () {
    const onChange = this.onChange
    const {isLoading} = this.state
    return this.props.render({onChange, isLoading})
  }
}

export default FileUpload
