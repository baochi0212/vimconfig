return {version=12,pkgs={{dir="/home/ubuntu/.local/share/nvim/lazy/astrocore",source="lazy",name="astrocore",spec=function()
return {
  "AstroNvim/astrocore",
  opts_extend = {
    "rooter.ignore.servers",
    "rooter.ignore.dirs",
    "sessions.ignore.buftypes",
    "sessions.ignore.dirs",
    "sessions.ignore.filetypes",
    "git_worktrees",
  },
}

end,file="lazy.lua",},{dir="/home/ubuntu/.local/share/nvim/lazy/astrolsp",source="lazy",name="astrolsp",spec=function()
return {
  "AstroNvim/astrolsp",
  opts_extend = {
    "formatting.disabled",
    "formatting.format_on_save.allow_filetypes",
    "formatting.format_on_save.ignore_filetypes",
    "servers",
  },
}

end,file="lazy.lua",},{dir="/home/ubuntu/.local/share/nvim/lazy/plenary.nvim",source="lazy",name="plenary.nvim",spec={"nvim-lua/plenary.nvim",lazy=true,},file="community",},{dir="/home/ubuntu/.local/share/nvim/lazy/telescope.nvim",source="rockspec",name="telescope.nvim",spec={"telescope.nvim",build=false,specs={{"nvim-lua/plenary.nvim",lazy=true,},},},file="telescope.nvim-scm-1.rockspec",},},}