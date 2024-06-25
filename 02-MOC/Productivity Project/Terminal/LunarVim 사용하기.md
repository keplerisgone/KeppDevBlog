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