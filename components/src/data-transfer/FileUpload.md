```js
<FileUpload
  onFileLoad={file => console.log('Loaded file:', file)}
  render={({onChange, isLoading}) => isLoading
  ? <div>LOADING FILE...</div>
  : <input type='file' onChange={onChange} />
  }
/>
```
