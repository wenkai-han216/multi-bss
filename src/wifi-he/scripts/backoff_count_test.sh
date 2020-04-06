#!/bin/bash
source spatial-reuse-functions.sh
cd ../examples
export AUTO_DELETE_SPATIAL_REUSE_OUTPUT_FILES=1

export enablePcap=0
export enableAscii=1
export rxSensitivity=-90
export standard=11ac

obssPdLevel=-82
#export NS_LOG=DynamicObssPdAlgorithm=logic


RngRunpar=1
npar=1
Res=Sim0

export enableFrameCapture=true
export powerBackoff=0
export RngRun=${RngRunpar}
export obssPdAlgorithm=ConstantObssPdAlgorithm
export obssPdThreshold=-74
export maxAmpduSize=65535
export MCS=0
export downlink=0
export uplink=400
export duration=20
export enableRts=0
export txStartOffset=50
export enableObssPd=0
export txGain=0
export rxGain=0
export antennas=1
export maxSupportedTxSpatialStreams=1
export maxSupportedRxSpatialStreams=1
export performTgaxTimingChecks=1
export nodePositionsFile=NONE
export bw=20
export scenario=logdistance
export nBss=3
export payloadSizeUplink=1472
export payloadSizeDownlink=1508
export useIdealWifiManager=0
export r=0.1
export powSta=20
export powAp=20
export txRange=102
export ccaTrSta=-82
export ccaTrAp=-82
export d=5
export sigma=0.0
export bianchi=1
export n=${npar}
export enableObssPd=0
export test=${Res}_${RngRun}
run_one 

wait
done
done
