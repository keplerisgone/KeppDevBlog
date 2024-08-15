Lunarvim은 Neovim의 강력한 플러그인 관리 및 구성 시스템을 제공하는 프레임워크입니다. Lunarvim을 처음부터 끝까지 설치하고 설정하는 과정을 안내드리겠습니다.

### 1. 필수 구성 요소 설치

먼저, Lunarvim을 사용하기 위해 필요한 몇 가지 프로그램들을 설치해야 합니다.

#### 1.1 Neovim 설치
Neovim은 Lunarvim의 기반이 되는 텍스트 에디터입니다. 아래 명령어를 사용하여 Neovim을 설치할 수 있습니다.

```sh
# Ubuntu
sudo apt update
sudo apt install neovim

# macOS (Homebrew)
brew install neovim
```

#### 1.2 Node.js, npm, and yarn 설치
Lunarvim은 일부 플러그인을 위해 Node.js와 npm을 필요로 합니다. yarn도 설치해야 합니다.

```sh
# Ubuntu
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm install -g yarn

# macOS (Homebrew)
brew install node
brew install yarn
```

#### 1.3 Packer.nvim 설치
Lunarvim은 Packer.nvim이라는 플러그인 관리자를 사용합니다. 이를 설치해야 합니다.

```sh
git clone --depth 1 https://github.com/wbthomason/packer.nvim\
  ~/.local/share/nvim/site/pack/packer/start/packer.nvim
```

### 2. Lunarvim 설치

이제 Lunarvim을 설치할 차례입니다. Lunarvim의 설치 스크립트를 실행합니다.

```sh
bash <(curl -s https://raw.githubusercontent.com/LunarVim/LunarVim/master/utils/installer/install.sh)
```

### 3. 환경 설정

#### 3.1 Lunarvim 설정 파일
Lunarvim 설정 파일은 `~/.config/lvim/config.lua`에 있습니다. 이 파일을 열어 필요한 설정을 추가하거나 변경할 수 있습니다.

```sh
nvim ~/.config/lvim/config.lua
```

기본 설정은 다음과 같습니다:

```lua
-- general
lvim.log.level = "warn"
lvim.format_on_save = true
lvim.colorscheme = "tokyonight"

-- keymappings
lvim.leader = "space"
-- add your own keymapping

-- use which-key to add extra bindings with the leader-key prefix
lvim.builtin.which_key.mappings["P"] = { "<cmd>Telescope projects<CR>", "Projects" }

-- Enable Telescope fuzzy finder
lvim.builtin.telescope.active = true

-- Add Treesitter language parsers
lvim.builtin.treesitter.ensure_installed = {
  "bash",
  "c",
  "javascript",
  "json",
  "lua",
  "python",
  "typescript",
  "tsx",
  "css",
  "rust",
  "java",
  "yaml",
}

-- set a formatter
local formatters = require "lvim.lsp.null-ls.formatters"
formatters.setup {
  { command = "prettier", filetypes = { "typescript", "typescriptreact" } },
}

-- set a linter
local linters = require "lvim.lsp.null-ls.linters"
linters.setup {
  { command = "eslint", filetypes = { "typescript", "typescriptreact" } },
}
```

### 4. 추가 플러그인 설치

Lunarvim의 강점 중 하나는 쉽게 플러그인을 추가할 수 있다는 점입니다. `~/.config/lvim/config.lua` 파일에 플러그인을 추가할 수 있습니다.

예를 들어, `nvim-tree.lua`를 추가하고 싶다면 다음과 같이 설정할 수 있습니다:

```lua
lvim.plugins = {
    {"kyazdani42/nvim-tree.lua"},
}
```

### 5. 플러그인 설치 및 업데이트

Lunarvim 설정을 저장한 후, Neovim을 열어 플러그인을 설치합니다.

```sh
lvim +PackerSync
```

### 6. Neovim 사용 시작

설치가 완료되면 `nvim` 명령어로 Neovim을 실행하고 Lunarvim 환경을 사용하여 코드를 작성할 수 있습니다.

```sh
nvim
```

이제 Lunarvim을 통해 강력한 Neovim 환경을 즐길 수 있습니다. 필요에 따라 설정 파일을 수정하고, 플러그인을 추가하면서 자신만의 커스터마이즈된 개발 환경을 만들어 나가세요.

# C++ 개발 환경 만들기

Lunarvim에서 C++ 개발을 위해 필요한 추가 설정을 설명드리겠습니다. C++ 개발을 위해서는 언어 서버 프로토콜(LSP), 자동 완성, 디버깅 등을 설정하는 것이 중요합니다. 아래는 Lunarvim을 C++ 개발에 맞게 설정하는 방법입니다.

### 1. C++ 언어 서버 설치

먼저, C++ 언어 서버를 설치해야 합니다. 가장 많이 사용되는 언어 서버는 `clangd`입니다. `clangd`는 C, C++, Objective-C 언어를 위한 LSP 서버입니다.

#### 1.1 Clangd 설치

##### Ubuntu:
```sh
sudo apt install clangd
```

##### macOS (Homebrew):
```sh
brew install llvm
```
설치 후, `clangd`를 PATH에 추가합니다.
```sh
echo 'export PATH="/usr/local/opt/llvm/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### 2. Lunarvim 설정

`~/.config/lvim/config.lua` 파일을 열어 C++ 개발을 위한 설정을 추가합니다.

```lua
-- ~/.config/lvim/config.lua

-- general
lvim.log.level = "warn"
lvim.format_on_save = true
lvim.colorscheme = "tokyonight"

-- keymappings
lvim.leader = "space"

-- which-key mappings
lvim.builtin.which_key.mappings["P"] = { "<cmd>Telescope projects<CR>", "Projects" }

-- Enable Telescope fuzzy finder
lvim.builtin.telescope.active = true

-- Add Treesitter language parsers
lvim.builtin.treesitter.ensure_installed = {
  "bash",
  "c",
  "javascript",
  "json",
  "lua",
  "python",
  "typescript",
  "tsx",
  "css",
  "rust",
  "java",
  "yaml",
  "cpp",  -- C++ 추가
}

-- set a formatter
local formatters = require "lvim.lsp.null-ls.formatters"
formatters.setup {
  { command = "clang-format", filetypes = { "c", "cpp", "objc", "objcpp" } },
}

-- set a linter
local linters = require "lvim.lsp.null-ls.linters"
linters.setup {
  { command = "clang-tidy", filetypes = { "c", "cpp", "objc", "objcpp" } },
}

-- LSP 설정
local lspconfig = require "lspconfig"
lspconfig.clangd.setup {}

-- Additional Plugins
lvim.plugins = {
    {"kyazdani42/nvim-tree.lua"},
    {"hoob3rt/lualine.nvim"},
}
```

### 3. CMake 설정

C++ 프로젝트에서는 빌드 시스템으로 CMake를 많이 사용합니다. CMake를 설정하여 편리하게 빌드할 수 있도록 합니다.

#### 3.1 CMake 설치

##### Ubuntu:
```sh
sudo apt install cmake
```

##### macOS (Homebrew):
```sh
brew install cmake
```

#### 3.2 CMake 플러그인 추가

`~/.config/lvim/config.lua` 파일에 CMake 관련 플러그인을 추가합니다.

```lua
-- Additional Plugins
lvim.plugins = {
    {"kyazdani42/nvim-tree.lua"},
    {"hoob3rt/lualine.nvim"},
    {"cdelledonne/vim-cmake"},  -- CMake 플러그인 추가
}
```

### 4. 디버깅 설정

디버깅을 위해 `nvim-dap` 플러그인을 설정합니다.

#### 4.1 nvim-dap 및 dap-cpptools 설치

`~/.config/lvim/config.lua` 파일에 디버깅 플러그인을 추가합니다.

```lua
-- Additional Plugins
lvim.plugins = {
    {"kyazdani42/nvim-tree.lua"},
    {"hoob3rt/lualine.nvim"},
    {"cdelledonne/vim-cmake"},
    {"mfussenegger/nvim-dap"},  -- nvim-dap 플러그인 추가
    {"rcarriga/nvim-dap-ui"},   -- nvim-dap-ui 플러그인 추가
    {"theHamsta/nvim-dap-virtual-text"}, -- 디버깅 가상 텍스트 플러그인 추가
    {"nvim-telescope/telescope-dap.nvim"}, -- Telescope 디버깅 플러그인 추가
}

-- DAP 설정
local dap = require('dap')
dap.adapters.cppdbg = {
  id = 'cppdbg',
  type = 'executable',
  command = 'path/to/cpptools/extension/debugAdapters/bin/OpenDebugAD7',  -- cpptools 경로
}

dap.configurations.cpp = {
  {
    name = "Launch file",
    type = "cppdbg",
    request = "launch",
    program = function()
      return vim.fn.input('Path to executable: ', vim.fn.getcwd() .. '/', 'file')
    end,
    cwd = '${workspaceFolder}',
    stopOnEntry = false,
    setupCommands = {
      {
        description = 'Enable pretty-printing for gdb',
        text = '-enable-pretty-printing',
        ignoreFailures = false
      },
    },
  },
}

-- DAP UI 설정
require("dapui").setup()
require("nvim-dap-virtual-text").setup()
```

위 설정으로 Lunarvim에서 C++ 개발을 위한 기본적인 환경을 구축할 수 있습니다. 이제 C++ 파일을 열고 작업할 수 있으며, LSP, 자동 완성, 디버깅 등의 기능을 사용할 수 있습니다.

`Failed to source /Users/zlzonpower/.local/share/lunarvim/site/pack/lazy/opt/nvim-treesitter/plugin/nvim-treesitter.lua` 에러 발생시 lvim 내부에서 `:Lazy sync` 입력으로 해결 가능!

하지만 많은 사람들이 LunarVim은 오류가 잦다고 탈출하는 모양이다.
[[Astronvim 사용하기]]로 가자!
