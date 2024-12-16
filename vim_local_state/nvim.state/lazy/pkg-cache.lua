return {pkgs={{dir="/home/ubuntu/.local/share/nvim/lazy/astrocore",name="astrocore",source="lazy",file="lazy.lua",spec=function()
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

end,},{dir="/home/ubuntu/.local/share/nvim/lazy/astrolsp",name="astrolsp",source="lazy",file="lazy.lua",spec=function()
return {
  "AstroNvim/astrolsp",
  opts_extend = {
    "formatting.disabled",
    "formatting.format_on_save.allow_filetypes",
    "formatting.format_on_save.ignore_filetypes",
    "servers",
  },
}

end,},{dir="/home/ubuntu/.local/share/nvim/lazy/plenary.nvim",name="plenary.nvim",source="lazy",file="community",spec={"nvim-lua/plenary.nvim",lazy=true,},},{dir="/home/ubuntu/.local/share/nvim/lazy/telescope.nvim",name="telescope.nvim",source="rockspec",file="telescope.nvim-scm-1.rockspec",spec={"telescope.nvim",specs={{"nvim-lua/plenary.nvim",lazy=true,},},build=false,},},},version=12,}