+ How to disp a vector
  + fprint

    `fmt = ['The vector P is: [', repmat('%g, ', 1, numel(P)-1), '%g]\n'];`
    `fprintf(fmt, P)`
