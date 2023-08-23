function require(moduleName) {
  console.log(`Require invoked for module: ${moduleName}`);
  const id = require.resolve(moduleName);
  if (require.cache[id]) {
    return require.cache[id].exports;
  }

  // module metadata
  const module = {
    exports: {},
    id,
  };
  // Update the cache
  require.cache[id] = module;

  // Load the module
  loadModule(id, module, require);

  // return exported variables
  return module.exports;
}
require.cache = {};
require.resolve = (moduleName) => {
  // resolve a full module id from the moduleName
};
