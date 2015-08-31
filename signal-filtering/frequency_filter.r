library(signal)
library(foreach)
library(doParallel)


filterFiles = function(indir, outdir, cutoff) {
  filterFile = function(indir, outdir, fname, cutoff) {
    data = read.csv(paste(indir, fname, sep = ""))
    lpf  = butter(3, cutoff)
    for (col in colnames(data)[2:length(colnames(data))]) {
      data[, c(col)] = filter(lpf, data[, c(col)])
    }
    write.csv(data, file = paste(outdir, fname, sep=""), row.names = FALSE, quote = FALSE)
  }
  
  for(fname in list.files(path = indir, pattern = "_data.csv")) {
    print(paste("processing", fname, "filter"))
    filterFile(indir, outdir, fname, cutoff)
  }
}

main = function() {
  cl<-makeCluster(8)
  registerDoParallel(cl)
  
  args = commandArgs(TRUE)
  if (length(args) != 1) {
    print("run command")
    print("Rscript frequency_filter.r cutoff")
  } else {
    filterFiles("~/Documents/dataset/EEG/input/train/", "~/Documents/dataset/EEG/input/train_filter/", as.numeric(args[1]))
    filterFiles("~/Documents/dataset/EEG/input/test/", "~/Documents/dataset/EEG/input/test_filter/", as.numeric(args[1]))
  }
}

main()

