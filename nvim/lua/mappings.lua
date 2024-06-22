require "nvchad.mappings"

-- add yours here

local map = vim.keymap.set

map("n", ";", ":", { desc = "CMD enter command mode" })
map("i", "jk", "<ESC>")

-- map({ "n", "i", "v" }, "<C-s>", "<cmd> w <cr>")
vim.api.nvim_set_keymap('n', 'qq', ':q<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('t', '<C-d>', '<C-\\><C-n>:q<CR>', { noremap = true, silent = true })

-- Ejecutar Live Server
-- Ejecutar Live Server en la carpeta actual
function StartLiveServer()
    local cwd = vim.fn.expand('%:p:h')  -- Obtener la ruta de la carpeta del archivo actual
    local cmd = 'live-server'
    local job_id = vim.fn.jobstart(cmd, {
        cwd = cwd,      -- Establecer el directorio de trabajo actual
        detached = true -- Ejecutar en segundo plano
    })
    print('Live Server iniciado en la carpeta:', cwd)
end

-- Asignar un atajo para iniciar Live Server
vim.api.nvim_set_keymap('n', '<leader>ls', ':lua StartLiveServer()<CR>', { silent = true })



vim.api.nvim_create_autocmd({ "InsertLeave", "TextChanged" }, {
  pattern = { "*" },
  command = "silent! wall",
  nested = true,
})
