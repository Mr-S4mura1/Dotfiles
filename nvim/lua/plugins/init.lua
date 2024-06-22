return {
  {
    "stevearc/conform.nvim",
    config = function()
      require "configs.conform"
    end,
  },

  -- These are some examples, uncomment them if you want to see them work!
  -- {
  --   "neovim/nvim-lspconfig",
  --   config = function()
  --     require("nvchad.configs.lspconfig").defaults()
  --     require "configs.lspconfig"
  --   end,
  -- },
  --
  -- {
  --    "williamboman/mason.nvim",
  --    opts = {
  --            ensure_installed = {
  --                    "lua-language-server", "stylua",
  --                    "html-lsp", "css-lsp" , "prettier"
  --            },
  --    },
  -- },
  --
  -- {
  --    "nvim-treesitter/nvim-treesitter",
  --    opts = {
  --            ensure_installed = {
  --                    "vim", "lua", "vimdoc",
  --      "html", "css"
  --            },
  --    },
  -- },

  {
    "m4xshen/hardtime.nvim",
    dependencies = { "MunifTanjim/nui.nvim", "nvim-lua/plenary.nvim" },
    opts = {}
  },

  {
    "nvimdev/guard.nvim",
    dependencies = {
        "nvimdev/guard-collection",
  },
  {
    'windwp/nvim-autopairs',
    event = "InsertEnter",
    opts = {}
  },

  { 
     "williamboman/mason.nvim", 
     opts = function(_, opts) 
       vim.list_extend(opts.ensure_installed, { "pyright", "black" }) 
     end, 
  }, 
  
   -- Setup null-ls with `black` 
  { 
     "jose-elias-alvarez/null-ls.nvim", 
     opts = function(_, opts) 
       local nls = require("null-ls") 
       opts.sources = vim.list_extend(opts.sources, { nls.builtins.formatting.black }) 
     end, 
  },

}
}

