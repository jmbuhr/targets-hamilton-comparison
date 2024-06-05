# _targets.R file
library(targets)
source("R/functions.R")
list(
  tar_target(file, "./data/data.csv", format = "file"),
  tar_target(data, get_data(file)),
  tar_target(model, fit_model(data)),
  tar_target(plot, plot_model(model, data))
)
